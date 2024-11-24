import pandas as pd
import numpy as np
import simpy


class Station(simpy.Store):
    """站点类，继承自simpy.Store。

    属性:
        env: simpy环境。
        name: 站点名称。
        station_id: 站点ID。
        next_station_distance: 到下一站的距离。
        station_info: 站点信息。

    方法:
        该类没有定义新的方法，只继承了simpy.Store的方法。
    """

    def __init__(self, env, name, station_id, next_station_distance):
        super().__init__(env)
        self.name = name
        self.station_id = station_id
        self.next_station_distance = next_station_distance
        self.station_info = pd.DataFrame()


class Passenger:
    """乘客类。

    属性:
        env: simpy环境。
        boarding_time: 上车时间。
        boarding_station_id: 上车站点ID。
        alighting_station_id: 下车站点ID。
        onboarding_time: 上车所需时间。
        alighting_time: 下车所需时间。
    法:
        arrive_station(self, boarding_station_id, stations_list): 乘客到达站点并等待上车。
    """

    def __init__(self, env, boarding_time, boarding_station_id, alighting_station_id):
        self.env = env
        self.boarding_time = boarding_time
        self.boarding_station_id = boarding_station_id
        self.alighting_station_id = alighting_station_id
        self.onboarding_time = np.random.lognormal(np.log(1.5), 0.5)
        self.alighting_time = np.random.lognormal(np.log(1.5), 0.5)

    def arrive_station(self, boarding_station_id, stations_list):
        """乘客到达站点并等待上车。

        Args:
            boarding_station_id: 上车站点ID。
            stations_list: 站点列表。
        """
        yield self.env.timeout(self.boarding_time)  # 等待上车时间
        yield stations_list[boarding_station_id].put(self)  # 进入站点


class Bus(simpy.Store):
    """公交车类，继承自simpy.Store。

    属性:
        env: simpy环境。
        bus_number: 公交车编号。
        speed: 公交车速度。
        current_station_index: 当前站点索引。
        next_station_index: 下一站点索引。
        current_passenger_count: 当前乘客数量。
        total_passenger_count: 总乘客数量。
        utilization_rates: 利用率列表。
    方法:
        start_bus(self): 每隔900 * bus_number秒后发车。
        move_to_next_station(self, current_station): 公交车移动到下一站。
        board_passengers(self, start_time, current_station): 多个乘客上车。
        alight_passengers(self, start_time, current_station): 多个乘客下车。
        process_passengers_at_station(self, current_station): 在一个站点处理乘客。
        board_and_alight_passengers(self, stations_list): 乘客上下车，并移动到下一站。计算局部和全局利用率。
    """

    def __init__(self, env, bus_number, speed):
        super().__init__(env, capacity=90)
        self.env = env
        self.bus_number = bus_number
        self.speed = speed
        self.current_station_index = 0
        self.next_station_index = 1
        self.current_passenger_count = 0
        self.total_passenger_count = 0
        self.bus_info = pd.DataFrame()
        self.global_utilization_rate = 0

    def start_bus(self):
        """每隔900 * bus_number秒后发车"""
        yield self.env.timeout(900 * self.bus_number)
        print(f'Bus {self.bus_number} starts at {self.env.now}')
        self.env.process(self.board_and_alight_passengers(stations))

    def move_to_next_station(self, current_station):
        """公交车移动到下一站。

        Args:
            current_station: 当前站点。
        """
        yield self.env.timeout(9)
        travel_time = current_station.next_station_distance / self.speed
        yield self.env.timeout(travel_time)
        yield self.env.timeout(9)
        self.current_station_index = self.next_station_index
        self.next_station_index += 1

    def board_passengers(self, start_time, current_station):
        """多个乘客上车。"""
        boarding_count = 0
        while self.env.now - start_time < 30:
            boarded = False  # 设置一个标志，表示是否有乘客上车
            for passenger in list(current_station.items):
                if self.current_passenger_count >= self.capacity:
                    break
                yield self.env.timeout(passenger.onboarding_time)
                self.items.append(passenger)
                current_station.items.remove(passenger)
                self.current_passenger_count += 1
                boarded = True
                boarding_count += 1
            if not boarded:
                break

        self.bus_info.loc[self.current_station_index, 'boarding_count'] = boarding_count
        current_station.station_info.loc[self.bus_number, 'boarding_count'] = boarding_count

    def alight_passengers(self, start_time, current_station):
        """多个乘客下车。"""
        alighting_count = 0
        while self.env.now - start_time <= 30:
            alighted = False  # 设置一个标志，表示是否有乘客下车
            for passenger in list(self.items):
                if passenger.alighting_station_id <= self.current_station_index:
                    yield self.env.timeout(passenger.alighting_time)
                    self.items.remove(passenger)
                    self.current_passenger_count -= 1
                    alighted = True
                    alighting_count += 1
                    self.total_passenger_count += 1
            if not alighted:
                break
        self.bus_info.loc[self.current_station_index, 'alighting_count'] = alighting_count
        current_station.station_info.loc[self.bus_number, 'alighting_count'] = alighting_count

    def process_passengers_at_station(self, current_station):
        """在一个站点处理乘客。

        Args:
            current_station: 当前站点。
        """
        arrival_time = self.env.now
        self.bus_info.loc[self.current_station_index, 'station_id'] = current_station.station_id
        self.bus_info.loc[self.current_station_index, 'arrival_time'] = arrival_time
        self.bus_info.loc[self.current_station_index, 'passenger_count_before'] = self.current_passenger_count
        current_station.station_info.loc[self.bus_number, 'bus_id'] = self.bus_number
        current_station.station_info.loc[self.bus_number, 'arrival_time'] = arrival_time
        current_station.station_info.loc[self.bus_number, 'passenger_count_before'] = self.current_passenger_count

        boarding_process = self.env.process(self.board_passengers(arrival_time, current_station))
        alighting_process = self.env.process(self.alight_passengers(arrival_time, current_station))
        yield self.env.all_of([boarding_process, alighting_process])

        departure_time = self.env.now
        self.bus_info.loc[self.current_station_index, 'departure_time'] = departure_time
        self.bus_info.loc[self.current_station_index, 'residence_time'] = departure_time - arrival_time
        self.bus_info.loc[self.current_station_index, 'passenger_count_after'] = self.current_passenger_count
        self.bus_info.loc[self.current_station_index, 'utilization_rate'] = self.current_passenger_count / self.capacity
        current_station.station_info.loc[self.bus_number, 'departure_time'] = departure_time
        current_station.station_info.loc[self.bus_number, 'residence_time'] = departure_time - arrival_time
        current_station.station_info.loc[self.bus_number, 'passenger_count_after'] = self.current_passenger_count
        current_station.station_info.loc[
            self.bus_number, 'utilization_rate'] = self.current_passenger_count / self.capacity

    def board_and_alight_passengers(self, stations_list):
        """乘客上下车，并移动到下一站。计算局部和全局利用率。

        Args:
            stations_list: 站点列表。
        """
        while self.current_station_index < len(stations_list):
            current_station = stations_list[self.current_station_index]
            yield from self.process_passengers_at_station(current_station)
            yield self.env.process(self.move_to_next_station(current_station))
        yield self.env.process(self.alight_passengers(self.env.now, stations_list[-1]))
        if self.current_passenger_count > 0:
            print(f'Warning: There are still{len(self.items)} passengers on the bus{self.bus_number}')
        global total_distance
        self.global_utilization_rate = sum(
            self.bus_info['utilization_rate'][i] * stations_list[i].next_station_distance / total_distance
            for i in range(48))
        print(f'Bus {self.bus_number} finished at {self.env.now} with utilization rate {self.global_utilization_rate}')


def create_stations(env):
    """创建站点列表。计算总距离。

    Args:
        env: simpy环境。

    Returns:
        stations: 站点列表。
    """
    data = pd.read_csv('Data/station_info_line_1.csv', header=0,
                       names=['id', 'name', 'longitude', 'latitude', 'distance'])
    stations_list = [Station(env, row['name'], row['id'], row['distance']) for index, row in data.iterrows()]
    global total_distance
    total_distance = sum(station.next_station_distance for station in stations_list)
    return stations_list


def create_passengers(env, date_id, stations_list):
    """创建乘客列表。

    Args:
        env: simpy环境。
        date_id: 日期ID。
        stations_list: 站点列表。

    Returns:
        passengers: 乘客列表。
    """
    data = pd.read_csv('Data/passenger_info_line1_day1.csv', header=0,
                       names=['date_id', 'order_id', 'boarding_station_id', 'boarding_station_name', 'boarding_time',
                              'alighting_station_id', 'alighting_station_name', 'alighting_time'])
    data = data[data['date_id'] == date_id]
    passengers_list = [Passenger(env, row['boarding_time'], row['boarding_station_id'], row['alighting_station_id']) for
                       index, row in data.iterrows()]
    for passenger in passengers_list:
        boarding_station_id = passenger.boarding_station_id
        env.process(passenger.arrive_station(boarding_station_id, stations_list))
    return passengers_list


def create_buses(env, num_buses, speed):
    """创建公交车并启动发车进程

    Args:
        env: simpy环境。
        num_buses: 公交车数量。
        speed: 公交车速度。

    Returns:
        buses: 公交车列表。
    """
    buses_list = []
    for i in range(num_buses):
        bus = Bus(env, i, speed)
        env.process(bus.start_bus())
        buses_list.append(bus)
    return buses_list


total_distance = 0
env_ = simpy.Environment()
stations = create_stations(env_)
passengers = create_passengers(env_, 1, stations)
buses = create_buses(env_, 61, 10)

env_.run(until=16.5 * 60 * 60)

print('Simulation completed!')


#%%

def export_info_to_csv(buses_list, stations_list):
    """导出前5个公交车和所有站点的信息为CSV文件。

    Args:
        buses_list: 公交车列表。
        stations_list: 站点列表。
    """
    for i, bus in enumerate(buses_list):
        bus.bus_info.to_csv(f'output_data/bus_{i}_info.csv', index=False)

    for i, station in enumerate(stations_list):
        station.station_info.to_csv(f'output_data/station_{i}_info.csv', index=False)


export_info_to_csv(buses, stations)


#%%
def calculate_number(buses_list):
    num = 0
    for bus in buses_list:
        num += bus.total_passenger_count
    print(num)


calculate_number(buses)


#%%
def export_bus_utilization_to_csv(buses_list):
    """导出每辆车的总利用率为CSV文件。

    Args:
        buses_list: 公交车列表。
    """
    data = {
        'Bus Number': [],
        'Total Passengers': [],
        'Total Utilization Rate': [],
    }
    for bus in buses_list:
        data['Bus Number'].append(bus.bus_number)
        data['Total Passengers'].append(bus.total_passenger_count)
        data['Total Utilization Rate'].append(bus.global_utilization_rate)

    df = pd.DataFrame(data)
    df.to_csv('output_data/all_buses_info.csv',index=False)


def export_station_info_to_csv(stations_list):
    """导出每个站点的信息为CSV文件。

    Args:
        stations_list: 站点列表。
    """
    data = {
        'Station ID': [],
        'Total Boarding Passengers': [],
        'Total Alighting Passengers': [],
        'Average Utilization Rate': [],
    }
    for station in stations_list:
        data['Station ID'].append(station.station_id)
        data['Total Boarding Passengers'].append(station.station_info['boarding_count'].sum())
        data['Total Alighting Passengers'].append(station.station_info['alighting_count'].sum())
        data['Average Utilization Rate'].append(station.station_info['utilization_rate'].mean())

    df = pd.DataFrame(data)
    df.to_csv('output_data/all_stations_info.csv',index=False)

# 如果需要导出数据，请取消下面两行代码的注释：

# export_station_info_to_csv(stations)
# export_bus_utilization_to_csv(buses)

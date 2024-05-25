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
    """

    def __init__(self, env, name, station_id, next_station_distance):
        super().__init__(env)
        self.name = name
        self.station_id = station_id
        self.next_station_distance = next_station_distance
        self.station_info = []


class Passenger:
    """乘客类。

    属性:
        env: simpy环境。
        boarding_time: 上车时间。
        boarding_station_id: 上车站点ID。
        alighting_station_id: 下车站点ID。
        onboarding_time: 上车所需时间。
        alighting_time: 下车所需时间。
    """

    def __init__(self, env, boarding_time, boarding_station_id, alighting_station_id):
        self.env = env
        self.boarding_time = boarding_time
        self.boarding_station_id = boarding_station_id
        self.alighting_station_id = alighting_station_id
        self.onboarding_time = np.random.normal(1.5, 0.5)
        self.alighting_time = np.random.normal(1.5, 0.5)

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
    """

    def __init__(self, env, bus_number, speed):
        super().__init__(env, capacity=30)
        self.env = env
        self.bus_number = bus_number
        self.speed = speed
        self.current_station_index = 0
        self.next_station_index = 1
        self.current_passenger_count = 0
        self.total_passenger_count = 0
        self.bus_info = []

    def start_bus(self):
        """每隔900 * bus_number秒后发车"""
        yield self.env.timeout(900 * self.bus_number)
        yield self.env.process(self.board_and_alight_passengers(stations))

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

    def board_single_passenger(self, current_station):
        """单个乘客上车。"""
        passenger = yield current_station.get()
        if self.current_passenger_count >= self.capacity:
            raise Exception('Bus is full')
        yield self.env.timeout(passenger.onboarding_time)
        yield self.put(passenger)
        self.current_passenger_count += 1
        self.total_passenger_count += 1

    def board_passengers(self, start_time, current_station):
        """多个乘客上车。"""
        while self.env.now - start_time < 15:
            if len(current_station.items) > 0:
                yield from self.board_single_passenger(current_station)
            if self.env.now - start_time >= 15:
                break

        if len(stations[self.current_station_index].items) > 0:
            while self.env.now - start_time < 30:
                if len(current_station.items) > 0:
                    yield from self.board_single_passenger(current_station)
                if self.env.now - start_time >= 30:
                    break

    def alight_single_passenger(self):
        """单个乘客下车。"""
        for passenger in list(self.items):
            if passenger.alighting_station_id == self.current_station_index:
                yield self.env.timeout(passenger.alighting_time)
                self.items.remove(passenger)
                self.current_passenger_count -= 1

    def alight_passengers(self):
        """多个乘客下车。"""
        start_time = self.env.now
        while self.env.now - start_time < 15:
            yield from self.alight_single_passenger()
            if self.env.now - start_time >= 15:
                break
        if any(passenger.alighting_station_id == self.current_station_index for passenger in self.items):
            while self.env.now - start_time < 30:
                yield from self.alight_single_passenger()
                if self.env.now - start_time >= 30:
                    break

    def collect_bus_info(self, station, arrival_time, departure_time):
        """收集公交车信息。

        Args:
            station: 当前站点。
            arrival_time: 到达时间。
            departure_time: 离开时间。
        """
        boarding_count = len(
            [passenger for passenger in self.items if passenger.boarding_station_id == station.station_id])
        alighting_count = len(
            [passenger for passenger in self.items if passenger.alighting_station_id == station.station_id])
        passenger_count_after_alighting = self.current_passenger_count
        utilization_rate = passenger_count_after_alighting / self.capacity

        self.bus_info.append({
            'Arrival Time': arrival_time,
            'Departure Time': departure_time,
            'Boarding Count': boarding_count,
            'Alighting Count': alighting_count,
            'Passenger Count After Alighting': passenger_count_after_alighting,
            'Utilization Rate': utilization_rate,
        })

    def update_station_info(self, current_station, arrival_time, departure_time):
        """更新站点信息。

        Args:
            current_station: 当前站点。
            arrival_time: 到达时间。
            departure_time: 离开时间。
        """
        boarding_count = len(
            [passenger for passenger in self.items if passenger.boarding_station_id == current_station.station_id])
        alighting_count = len(
            [passenger for passenger in self.items if passenger.alighting_station_id == current_station.station_id])
        current_station.station_info.append({
            'Bus Number': self.bus_number,
            'Arrival Time': arrival_time,
            'Departure Time': departure_time,
            'Boarding Count': boarding_count,
            'Alighting Count': alighting_count
        })

    def process_passengers_at_station(self, current_station):
        """在一个站点处理乘客。

        Args:
            current_station: 当前站点。
        """
        arrival_time = self.env.now
        boarding_process = self.env.process(self.board_passengers(arrival_time, current_station))
        alighting_process = self.env.process(self.alight_passengers())
        yield self.env.all_of([boarding_process, alighting_process])
        departure_time = self.env.now
        self.collect_bus_info(current_station, arrival_time, departure_time)
        self.update_station_info(current_station, arrival_time, departure_time)

    def board_and_alight_passengers(self, stations_list):
        """乘客上下车，并移动到下一站。计算局部和全局利用率。

        Args:
            stations_list: 站点列表。
        """
        while self.next_station_index < len(stations_list):
            current_station = stations_list[self.current_station_index]
            yield from self.process_passengers_at_station(current_station)
            yield self.env.process(self.move_to_next_station(current_station))
        yield self.env.process(self.alight_passengers())
        if self.current_passenger_count > 0:
            print(f'Warning: There are still{len(self.items)} passengers on the bus{self.bus_number}')
        global total_distance
        global_utilization_rate = sum(info['Utilization Rate'] * stations_list[i].next_station_distance / total_distance
                                      for i, info in enumerate(self.bus_info))
        return global_utilization_rate


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
    data = pd.read_csv('Data/passenger_info.csv', header=0,
                       names=['date_id', 'order_id', 'boarding_station_id', 'boarding_station_name', 'boarding_time',
                              'alighting_station_id', 'alighting_station_name', 'alighting_time'])
    data = data[data['date_id'] == date_id].head(20)
    passengers_list = [Passenger(env, row['boarding_time'], row['boarding_station_id'], row['alighting_station_id']) for
                       index, row in data.iterrows()]
    for passenger in passengers_list:
        boarding_station_id = passenger.boarding_station_id
        env.process(passenger.arrive_station(boarding_station_id, stations_list))
    return passengers_list


def create_buses(env, num_buses, speed):
    """一次性创建并启动所有的公交车。

    Args:
        env: simpy环境。
        num_buses: 公交车数量。
        speed: 公交车速度。

    Returns:
        buses: 公交车列表。
    """
    buses_list = []
    for i in range(num_buses):
        bus = Bus(env, i, speed)  # 创建新的公交车对象
        buses_list.append(bus)
        env.process(bus.start_bus())  # 添加新的过程
    return buses_list


total_distance = 0
env_ = simpy.Environment()
stations = create_stations(env_)
passengers = create_passengers(env_, 1, stations)
buses = create_buses(env_, 60, 60)

env_.run(until=15.5 * 60 * 60)


def export_info_to_csv(buses_list, stations_list):
    """导出前5个公交车和所有站点的信息为CSV文件。

    Args:
        buses_list: 公交车列表。
        stations_list: 站点列表。
    """
    # 导出前5个公交车的信息
    for i, bus in enumerate(buses_list[:5]):
        df = pd.DataFrame(bus.bus_info)
        df.to_csv(f'output_data/bus_{i}_info.csv')

    # 导出所有站点的信息
    for i, station in enumerate(stations_list):
        df = pd.DataFrame(station.station_info)
        df.to_csv(f'output_data/station_{i}_info.csv')


# export_info_to_csv(buses, stations)

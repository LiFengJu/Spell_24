import pandas as pd

df = pd.DataFrame(columns=["Column1", "Column2", "Column3"])


def collect_bus_info(self, current_station, arrival_time, departure_time):
    """收集公交车信息。

    Args:
        current_station: 当前站点。
        arrival_time: 到达时间。
        departure_time: 离开时间。
    """
    boarding_count = len(
        [passenger for passenger in self.items if passenger.boarding_station_id == current_station.station_id])
    alighting_count = len(
        [passenger for passenger in self.items if passenger.alighting_station_id == current_station.station_id])
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
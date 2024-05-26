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

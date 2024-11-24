import simpy
def request(user,servers,name):
    while True: 
        # 刷新用户开始等待的时间
        user.start_wait = user.env.now
        if user.level == 0:
            user.near_search(servers,name)
            yield user.env.process(send_request(user,user.near_servers))
            user.level += 1
        elif user.level == 1:
            user.near_search(servers,name)
            temp = user.near_servers
            user.level += 1
            user.near_search(servers,name)
            user.level -= 1
            yield user.env.process(send_request(user,temp))
            user.level += 1
        elif user.level == 2:
            if name == 'random':
                user.near_search(servers)
                yield user.env.process(send_request(user,user.random_one())) 
                user.status = True
            else:
                if user.near_servers:
                    yield user.env.process(send_request(user,user.near_servers))
                    user.status = True
                else:
                    user.near_search(servers,name)
                    yield user.env.process(send_request(user,user.near_servers))
                    user.status = True
            break

def send_request(user,search_servers):
    for server in search_servers:
                # 如果有空闲带宽，即刻开始服务
        if user.bandwidth_request <= server.bandwidth.level and server.service_flag:
            # 从服务器的带宽资源中申请带宽,并开始服务   
            with server.resource.request(priority=user.priority) as req:
                yield req
                yield user.env.process(server.serve(user))
                return
        else:
            server.users_waiting.append(user)

    # 如果用户没有被服务，且用户的优先级为0，尝试
    if user.priority == 0:
        for server in search_servers:
            if server.service_flag  and user.bandwidth_request <= server.bandwidth.level + server.max_bandwidth - server.balanced_bandwidth_limit:
                server.increase_bandwidth()
                with server.resource.request(priority=user.priority) as req:
                    yield req
                    yield user.env.process(server.serve(user))
                    # 服务完成后减少服务器带宽
                    server.service_flag = False
                    server.reduce_bandwidth()
                    return
    yield user.serve_over

import simpy

def f1(env):
    yield env.timeout(1)
    print(env.now, "f1")

def f2(env):
    yield env.timeout(2)
    print(env.now, "f2")

def f3(env):
    f1_process = env.process(f1(env))
    f2_process = env.process(f2(env))
    yield env.all_of([f1_process, f2_process])
    print(env.now, "f3")


env_ = simpy.Environment()
env_.process(f3(env_))
env_.run(until=5)

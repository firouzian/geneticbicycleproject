import allobjects as aob


t_i = 0.0
t_f = 10.0
dt  = 0.0001
t_steps = int((t_f-t_i)/dt)

a = aob.AllObjects()

for i in range (t_steps):
        a.update()
        
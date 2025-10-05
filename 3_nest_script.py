import matplotlib.pyplot as plt
import nest
neuron1 = nest.Create("iaf_psc_alpha")
neuron1.set(I_e=376.0)
neuron2 = nest.Create("iaf_psc_alpha")
multimeter = nest.Create("multimeter")
multimeter.set(record_from=["V_m"])

nest.Connect(neuron1, neuron2, syn_spec = {"weight":20.0, "delay":1.0})
nest.Connect(multimeter, neuron2)

nest.Simulate(1000.0)
dmm = multimeter.get()

Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]

plt.figure(1)
plt.plot(ts,Vms)
plt.xlabel("Время (мс)")
plt.ylabel("Мембранный потенциал (мВ)")
plt.title("Мембранный потенциал принимающего нейрона")
plt.grid(True)
plt.savefig("Связь двух нейронов.png")

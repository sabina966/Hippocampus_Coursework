
import matplotlib.pyplot as plt
import nest
neuron = nest.Create("iaf_psc_alpha")
neuron2 = nest.Create("iaf_psc_alpha")

neuron.get("I_e")
neuron.get(["V_reset", "V_th"])
neuron.set(I_e=0.0)

noise_ex = nest.Create("poisson_generator")
noise_in = nest.Create("poisson_generator")
noise_ex.set(rate=80000.0)
noise_in.set(rate=15000.0)

syn_dict_ex = {"weight": 1.2}
syn_dict_in = {"weight": -2.0}
nest.Connect(noise_ex, neuron, syn_spec=syn_dict_ex)
nest.Connect(noise_in, neuron, syn_spec=syn_dict_in)

#neuron2.get("I_e")
#neuron2.get(["V_reset", "V_th"])
#neuron2.set(I_e=576.0)

multimeter = nest.Create("multimeter")
multimeter.set(record_from=["V_m"])
#spikerecorder = nest.Create("spike_recorder")



nest.Connect(multimeter, neuron)
#nest.Connect(multimeter, neuron2)

#nest.Connect(neuron, spikerecorder)


nest.Simulate(1000.0)
dmm = multimeter.get()

Vms1 = dmm["events"]["V_m"]
ts1 = dmm["events"]["times"]
# print(Vms, ts)

#Vms2 = dmm["events"]["V_m"][1::2]
#ts2 = dmm["events"]["times"][1::2]


plt.figure(1)
plt.plot(ts1, Vms1)

plt.xlabel("Время (мс)")
plt.ylabel("Мембранный потенциал (мВ)")
plt.title("Мембранный потенциал одного нейрона")
plt.grid(True)
# Сохраняем первую фигуру в файл
plt.savefig("1membrane_potential.png")

#plt.figure(2)
#plt.plot(ts2, Vms2)

#plt.xlabel("Время (мс)")
#plt.ylabel("Мембранный потенциал (мВ)")
#plt.title("Мембранный потенциал одного нейрона")
#plt.grid(True)
# Сохраняем фигуру в файл
#plt.savefig("2membrane_potential.png")

#events = spikerecorder.get("events")
#senders = events["senders"]
#ts = events["times"]
#plt.figure(3)
#plt.plot(ts, senders,".")
#plt.xlabel("Время (мс)")
#plt.ylabel("Идентификатор нейрона (GID)")
#plt.title("Спайки одного нейрона")
#plt.grid(True)
# Сохраняем вторую фигуру в файл
#plt.savefig("spikes_raster_plot.png")



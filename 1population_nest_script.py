import matplotlib.pyplot as plt import nest import numpy as np

# Установим seed для воспроизводимости
np.random.seed(42) nest.SetKernelStatus({'rng_seeds': [42]})

# Настройка моделей нейронов
edict = {"I_e": 200.0, "tau_m": 20.0, "V_th": -55.0, "V_reset": -70.0} 
nest.CopyModel("iaf_psc_alpha", "exc_iaf_psc_alpha") nest.SetDefaults("exc_iaf_psc_alpha", 
edict)

idict = {"I_e": 300.0, "tau_m": 20.0, "V_th": -55.0, "V_reset": -70.0} 
nest.CopyModel("iaf_psc_alpha", "inh_iaf_psc_alpha") nest.SetDefaults("inh_iaf_psc_alpha", 
idict)

# Создание популяций
epop = nest.Create("exc_iaf_psc_alpha", 100) # 100 возбуждающих ipop = 
nest.Create("inh_iaf_psc_alpha", 100) # 100 тормозных

# Создаем мультиметр для записи потенциала
multimeter = nest.Create("multimeter") multimeter.set(record_from=["V_m"])

# Создаем детектор спайков
spike_detector = nest.Create("spike_recorder")

# Соединения
nest.Connect(ipop, epop, conn_spec={"rule": "fixed_indegree", "indegree": 10}, 
B             syn_spec={"weight": -2.0})

                          # Подключаем мультиметр к первому нейрону (без one_to_one)
                          nest.Connect(multimeter, epop[0:1])

                          # Подключаем детектор спайков ко всем нейронам
                          nest.Connect(epop, spike_detector)

                          # Симуляция
                          nest.Simulate(1000.0)

                          # Получение данных
                          events = multimeter.get("events") Vms = events["V_m"] ts = 
                          events["times"]

                          spike_data = spike_detector.get("events") spike_times = 
                          spike_data["times"] spike_senders = spike_data["senders"]

                          # Построение графиков
                          plt.figure(figsize=(12, 6))

                          # График мембранного потенциала
                          plt.subplot(2, 1, 1) plt.plot(ts, Vms) plt.axhline(y=-55.0, 
                          color='r', linestyle='--', label="Порог (V_th)") 
                          plt.ylabel("Мембранный потенциал (мВ)") plt.title("Динамика 
                          мембранного потенциала первого нейрона") plt.grid(True) 
                          plt.legend()

                          # График спайков
                          plt.subplot(2, 1, 2) plt.plot(spike_times, spike_senders, '|', 
                          markersize=10) plt.xlabel("Время (мс)") plt.ylabel("ID нейрона") 
                          plt.title("Спайки в популяции") plt.grid(True)

                          plt.tight_layout() plt.savefig("network_activity.png") plt.show()

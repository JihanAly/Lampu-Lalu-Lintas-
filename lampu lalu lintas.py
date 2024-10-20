import time

def status_lampu(detik, lampu):
    while detik > 0:
        print(f"\r{lampu} selama {detik} detik", end='') 
        time.sleep(1)
        detik -= 1
    print()  

def traffic_light_simulation():
    while True:
        status_lampu(5, "Lampu Merah")
        status_lampu(2, "Lampu Kuning")
        status_lampu(7, "Lampu Hijau")

if __name__ == "__main__":
    traffic_light_simulation()

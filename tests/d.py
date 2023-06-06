class CPU:  # класс для описания процессоров;
    def __init__(self, name, fr) -> None:
        self.name = name
        self.fr = fr


class Memory:  # класс для описания памяти;
    def __init__(self, name, volume) -> None:
        self.name = name
        self.volume = volume


class MotherBoard:  # класс для описания материнских плат.
    def __init__(self, name, cpu, *mem_slots, total_mem_slots=4) -> None:
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = total_mem_slots
        self.mem_slots = mem_slots[:total_mem_slots]

    def get_config(self):
        return print([f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память: {"; ".join([f"{i.name} - {i.volume}" for i in self.mem_slots])}'])


cpu = CPU('asus', 1333)
mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 4000)
mb = MotherBoard('Asus', cpu, mem1, mem2)
print(mb.get_config())


['Материнская плата: Asus',
 'Центральный процессор: asus, 1333',
 'Слотов памяти: 4',
 'Память: Kingstone - 4000; Kingstone - 4000']
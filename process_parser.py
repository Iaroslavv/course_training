import datetime
from subprocess import PIPE, Popen
import textwrap


class ProcessParser:
    def __init__(self, commands=None, users=[], number_processes=[],
                 users_processes={}, total_memory=0, cpu=0,
                most_memory=None, most_cpu=None):
        self.commands = commands
        self.users = users
        self.number_processes = number_processes
        self.users_processes = users_processes
        self.total_memory = total_memory # %
        self.cpu = cpu # %
        self.most_memory = most_memory
        self.most_cpu = most_cpu

    def run_process(self):
        cmd = Popen(self.commands, stdout=PIPE, stdin=PIPE,
                    encoding='utf-8', shell=True)
        result = cmd.stdout
        return result

    def calculate_data(self):
        result = self.run_process()
        most_memory = {}
        most_cpu = {}
        for line in result:
            splitted_line = line.split()
            user = splitted_line[0]
            memory = splitted_line[3]
            cpu = splitted_line[2]
            process_name = splitted_line[10:]
            if user not in self.users:
                self.users.append(user)
    
            self.number_processes.append(splitted_line)
            self.users_processes[user] = self.users_processes.get(user, 0) + 1
            self.total_memory += float(memory.replace(',', '.'))
            self.cpu += float(cpu.replace(',', '.'))
    
            most_memory[float(memory.replace(',', '.'))] = process_name
            most_cpu[float(cpu.replace(',', '.'))] = process_name
    
            self.most_memory = ' '.join(most_memory.get(max(k for k in most_memory.keys())))[:20]
            self.most_cpu = ' '.join(most_cpu.get(max(k for k in most_cpu.keys())))[:20]
        
def write_to_file(commands): 
    parser_ = ProcessParser(commands)
    file_name = f"{datetime.datetime.utcnow().strftime('%d-%m-%y-%H:%M')}-scan"
    with open(file_name + '.txt', 'w') as f:
        parser_.calculate_data()
        keys, values = zip(*parser_.users_processes.items())
        total_user_processes = ', '.join([str(user) + ": " + str(process) for user,process in zip(keys,values)])
        text_to_write = textwrap.dedent(f"""\
        Отчет о состоянии системы:
        Пользователи системы: {', '.join(parser_.users)}
        Процессов запущено: {len(parser_.number_processes)}
        Пользовательских процессов: {total_user_processes}
        Всего памяти используется: {round(parser_.total_memory, 1)} %
        Всего CPU используется: {round(parser_.cpu, 1)} %
        Больше всего памяти использует: {parser_.most_memory}
        Больше всего CPU использует: {parser_.most_cpu}
        """)
        print(text_to_write)
        f.write(text_to_write)

if __name__ == '__main__':
    write_to_file('ps aux | tail -n +2')

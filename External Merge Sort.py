import os
import heapq

def external_merge_sort(input_file, output_file, chunk_size=1000):
    temp_files = []
    
    # Фаза 1: создание отсортированных чанков
    with open(input_file, 'r') as f:
        chunk = []
        file_idx = 0
        for line in f:
            chunk.append(line.strip())
            if len(chunk) >= chunk_size:
                chunk.sort()
                temp_file = f"temp_{file_idx}.txt"
                with open(temp_file, 'w') as temp:
                    temp.write('\n'.join(chunk))
                temp_files.append(temp_file)
                chunk.clear()
                file_idx += 1
        
        if chunk:
            chunk.sort()
            temp_file = f"temp_{file_idx}.txt"
            with open(temp_file, 'w') as temp:
                temp.write('\n'.join(chunk))
            temp_files.append(temp_file)
    
    # Фаза 2: многопутевое слияние
    heap = []
    file_handles = []
    
    # Инициализация heap первыми строками из каждого файла
    for idx, temp_file in enumerate(temp_files):
        f = open(temp_file, 'r')
        file_handles.append(f)
        line = f.readline().strip()
        if line:
            heapq.heappush(heap, (line, idx))
    
    with open(output_file, 'w') as out:
        while heap:
            smallest, file_idx = heapq.heappop(heap)
            out.write(smallest + '\n')
            next_line = file_handles[file_idx].readline().strip()
            if next_line:
                heapq.heappush(heap, (next_line, file_idx))
    
    # Закрытие временных файлов и их удаление
    for f in file_handles:
        f.close()
    for temp_file in temp_files:
        os.remove(temp_file)

# Пример использования
if __name__ == "__main__":
    # Создаём тестовый файл с числами
    with open('large_input.txt', 'w') as f:
        import random
        numbers = [str(random.randint(1, 100000)) for _ in range(10000)]
        f.write('\n'.join(numbers))
    
    external_merge_sort('large_input.txt', 'sorted_output.txt', chunk_size=1000)
    print("External merge sort завершён.")
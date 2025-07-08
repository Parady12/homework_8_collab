def chunking_by(numbers, chunck):
   
    result = []
    current_chunk = []
    count = 0

    for x in numbers:
        current_chunk.append(x)
        count += 1

        if count == chunck:
            result.append(current_chunk)
            current_chunk = []
            count = 0

        
    if current_chunk:
        result.append(current_chunk)

    return result



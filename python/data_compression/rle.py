# Run-Length Encoding

def encoder(content):
    if not content:
        return []
    # [(5, 3), (2, 2), (8, 4)] → [5, 5, 5, 2, 2, 8, 8, 8, 8]
    compressed_data = []

    prev = content[0]
    count = 1

    for curr in content[1:]:
        if curr == prev:
            count +=1
        else:
            compressed_data.append((prev, count))
            prev = curr
            count = 1
    return compressed_data + [(prev, count)]

def decoder(compressed_data):
    decompressed_data = []
    for char, count in compressed_data:
        decompressed_data += ([char] * count)
    return decompressed_data

def test_encoder():
    raw = [5, 5, 5, 2, 2, 8, 8, 8, 8]
    expected = [(5, 3), (2, 2), (8, 4)]
    compressed = encoder(raw)
    assert compressed == expected, f"expect={expected}, got={compressed}"

    raw = [5, 5, 5, 2, 2, 8, 8, 8, 8, 9]
    expected = [(5, 3), (2, 2), (8, 4), (9, 1)]
    compressed = encoder(raw)
    assert compressed == expected, f"expect={expected}, got={compressed}"

    raw = [1, 2, 3]
    expected = [(1, 1), (2, 1), (3, 1)]
    compressed = encoder(raw)
    assert compressed == expected, f"expect={expected}, got={compressed}"

    raw = [1, 1, 1, 1, 1]
    expected = [(1, 5)]
    compressed = encoder(raw)
    assert compressed == expected, f"expect={expected}, got={compressed}"

    raw = []
    expected = []
    compressed = encoder(raw)
    assert compressed == expected, f"expect={expected}, got={compressed}"

    print("Passed")

def test_decoder():
    compressed_data = [(5, 3), (2, 2), (8, 4)]
    expected = [5, 5, 5, 2, 2, 8, 8, 8, 8]
    decompressed = decoder(compressed_data)
    assert decompressed == expected, f"expect={expected}, got={decompressed}"

    compressed_data = [(5, 3), (2, 2), (8, 4), (9, 1)]
    expected = [5, 5, 5, 2, 2, 8, 8, 8, 8, 9]
    decompressed = decoder(compressed_data)
    assert decompressed == expected, f"expect={expected}, got={decompressed}"

    compressed_data = [(1, 1), (2, 1), (3, 1)]
    expected = [1, 2, 3]
    decompressed = decoder(compressed_data)
    assert decompressed == expected, f"expect={expected}, got={decompressed}"

    compressed_data = [(1, 5)]
    expected = [1, 1, 1, 1, 1]
    decompressed = decoder(compressed_data)
    assert decompressed == expected, f"expect={expected}, got={decompressed}"

    compressed_data = []
    expected = []
    decompressed = decoder(compressed_data)
    assert decompressed == expected, f"expect={expected}, got={decompressed}"

    print("Passed")


if __name__ == "__main__":
    test_encoder()
    test_decoder()

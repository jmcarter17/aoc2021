from day16 import hex_to_bin, parse_package, sum_versions, eval_tree


def compute_tree(raw):
    tree, _ = parse_package(raw, 0)
    return tree


def test_to_bin():
    assert hex_to_bin("D2FE28") == "110100101111111000101000"
    assert hex_to_bin("38006F45291200") == "00111000000000000110111101000101001010010001001000000000"
    assert hex_to_bin("EE00D40C823060") == "11101110000000001101010000001100100000100011000001100000"


def test_sum_versions():
    assert sum_versions(compute_tree(hex_to_bin("8A004A801A8002F478"))) == 16
    assert sum_versions(compute_tree(hex_to_bin("620080001611562C8802118E34"))) == 12
    assert sum_versions(compute_tree(hex_to_bin("C0015000016115A2E0802F182340"))) == 23
    assert sum_versions(compute_tree(hex_to_bin("A0016C880162017C3686B18A3D4780"))) == 31


def test_eval():
    assert eval_tree(compute_tree(hex_to_bin("C200B40A82"))) == 3
    assert eval_tree(compute_tree(hex_to_bin("04005AC33890"))) == 54
    assert eval_tree(compute_tree(hex_to_bin("880086C3E88112"))) == 7
    assert eval_tree(compute_tree(hex_to_bin("CE00C43D881120"))) == 9
    assert eval_tree(compute_tree(hex_to_bin("D8005AC2A8F0"))) == 1
    assert eval_tree(compute_tree(hex_to_bin("F600BC2D8F"))) == 0
    assert eval_tree(compute_tree(hex_to_bin("9C005AC2F8F0"))) == 0
    assert eval_tree(compute_tree(hex_to_bin("9C0141080250320F1802104A08"))) == 1

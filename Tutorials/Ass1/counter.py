import pprint

# Initialize counts for digraphs
count_digrams = {}

# Ciphertext provided
ciphertext = """WRTGNKHNDAKNMOCDBFKSFDSLEVKHFCBSKOCYOSGLPSLUSFNHFRFNSTCQTGHKLULUPRKIPTSVOSKDULKOKDSYKFSBKCSTFHMBSLFKBRXLFRPEFBFELAXCPMSBLEKDBWGSGXCPKBOXPBHDDAQDBRCDBFYOTSSBLOPE"""

# Count occurrences of digraphs
for i in range(0, len(ciphertext) - 1, 2):
    digram = ciphertext[i] + ciphertext[i + 1]
    if count_digrams.get(digram) is None:
        count_digrams[digram] = 1
    else:
        count_digrams[digram] += 1

# Sort digraphs by frequency of appearance in descending order
count_digrams = [[k, v] for k, v in count_digrams.items()]
count_digrams = sorted(count_digrams, key=lambda item: item[1], reverse=True)

# Print the sorted digraphs with their frequencies
pprint.pprint(count_digrams)

count_last = {}
for i in range(0, len(ciphertext) - 1, 2):
    digram = ciphertext[i] + ciphertext[i + 1]
    letter = ciphertext[i + 1]
    if count_last.get(letter) is None:
        count_last[letter] = [digram]
    else:
        count_last[letter].append(digram)

count_las = [[k, v] for k, v in count_last.items()]
count_las = sorted(count_las, key=lambda item: len(item[1]), reverse=True)

print("Last letter digrams")
pprint.pprint(count_las)

[['LU', 3],
 ['KD', 3],
 ['SB', 3],
 ['TG', 2],
 ['DA', 2],
 ['CD', 2],
 ['BF', 2],
 ['SL', 2],
 ['KO', 2],
 ['OS', 2],
 ['FR', 2],
 ['ST', 2],
 ['BR', 2],
 ['PE', 2],
 ['WR', 1],
 ['NK', 1],
 ['HN', 1],
 ['KN', 1],
 ['MO', 1],
 ['KS', 1],
 ['FD', 1],
 ['EV', 1],
 ['KH', 1],
 ['FC', 1],
 ['BS', 1],
 ['CY', 1],
 ['GL', 1],
 ['PS', 1],
 ['SF', 1],
 ['NH', 1],
 ['FN', 1],
 ['CQ', 1],
 ['HK', 1],
 ['PR', 1],
 ['KI', 1],
 ['PT', 1],
 ['SV', 1],
 ['UL', 1],
 ['SY', 1],
 ['KF', 1],
 ['KC', 1],
 ['FH', 1],
 ['MB', 1],
 ['FK', 1],
 ['XL', 1],
 ['FB', 1],
 ['FE', 1],
 ['LA', 1],
 ['XC', 1],
 ['PM', 1],
 ['LE', 1],
 ['BW', 1],
 ['GS', 1],
 ['GX', 1],
 ['CP', 1],
 ['KB', 1],
 ['OX', 1],
 ['PB', 1],
 ['HD', 1],
 ['QD', 1],
 ['YO', 1],
 ['TS', 1],
 ['LO', 1]]

[['D', ['CD', 'FD', 'KD', 'KD', 'KD', 'HD', 'QD', 'CD']],
 ['S', ['KS', 'BS', 'OS', 'PS', 'OS', 'GS', 'TS']],
 ['B', ['SB', 'MB', 'FB', 'SB', 'KB', 'PB', 'SB']],
 ['R', ['WR', 'FR', 'PR', 'BR', 'FR', 'BR']],
 ['O', ['MO', 'KO', 'KO', 'YO', 'LO']],
 ['L', ['SL', 'GL', 'UL', 'SL', 'XL']],
 ['F', ['BF', 'SF', 'KF', 'BF']],
 ['E', ['PE', 'FE', 'LE', 'PE']],
 ['K', ['NK', 'HK', 'FK']],
 ['N', ['HN', 'KN', 'FN']],
 ['A', ['DA', 'LA', 'DA']],
 ['H', ['KH', 'NH', 'FH']],
 ['C', ['FC', 'KC', 'XC']],
 ['U', ['LU', 'LU', 'LU']],
 ['T', ['ST', 'PT', 'ST']],
 ['G', ['TG', 'TG']],
 ['V', ['EV', 'SV']],
 ['Y', ['CY', 'SY']],
 ['X', ['GX', 'OX']],
 ['Q', ['CQ']],
 ['I', ['KI']],
 ['M', ['PM']],
 ['W', ['BW']],
 ['P', ['CP']]]
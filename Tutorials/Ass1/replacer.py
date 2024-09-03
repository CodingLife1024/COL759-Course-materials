def replacer(s, old_pair, new_pair, changed_list=[]):
    new_changes = []
    s = list(s)
    n = len(s)//2
    for i in range(len(s) - 1):
        if i not in changed_list and (i - 1) not in changed_list:
            if s[i] == old_pair[0] and s[i+1] == old_pair[1]:
                s[i] = new_pair[0]
                s[i+1] = new_pair[1]
                new_changes.append(i)
    return "".join(s), new_changes

# Example usage:
s = "SUMXER ANDX IDOWPBLV, YB SPBLSPNY CG FKDT NZ GTSM CG ANDX OPNDFKLULY. ANDX YBKFSFLV ZULY YPHTFECV, UBAN ANDX IDLN HRLULUOV TIRMRFSX KDNY NZ PTKCSC TIDXFYDX CIMXLUOV ANLGKMLZ ANDX GTDXPE. YB RLDTNY DM REDXPY GTUHSH, DXOSGLPS RLNYSPLN ZUBFHTNHSH, KDNY CDLMDPNY TIFDANFKURER WRBYLY THPO ANDX YPKULY. LU ANDX TYCDLUPR, YB QKANTSPS KHMNDA NZ FNOQBHST, LGDHBRER QUIHIQNHCXYI KDNY HRKHLUOV REGLSBLY. ANDX ULQRER YBST OXXC KDNY OCFDLV, UBAN ANDX RDZY BACNCN QC REKHLY. RB ZULY NZ YPNFFTNI PEFNYP THPO ANDX IARESC KDNY MIRESC QC TYTSDSDZ SLTF, NZ FLKDEF CG STOXLNDCEB UBAN DKBKST KDNY FDFL GCSFLV."

old_pair = "CY"
new_pair = "DX"
changed_list = [0, 2, 4, 269, 353, 7, 53, 70, 101, 104, 165, 174, 263, 284, 300, 320, 393, 430, 433, 493, 561, 9, 55, 72, 106, 149, 153, 176, 181, 202, 215, 286, 302, 395, 435, 495]

result, changes = replacer(s, old_pair, new_pair, changed_list)
print(result)
print(changes)

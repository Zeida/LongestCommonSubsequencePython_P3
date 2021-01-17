def LCS(first_word, second_word):
    matrix = [["" for x in range(len(second_word))] for x in range(len(first_word))]
    for i in range(len(first_word)):
        for j in range(len(second_word)):
            if first_word[i] == second_word[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = first_word[i]
                else:
                    matrix[i][j] = matrix[i-1][j-1] + first_word[i]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)

    lcs = matrix[-1][-1]

    return len(lcs), lcs

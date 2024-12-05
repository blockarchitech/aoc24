


with open("4.in", "r") as file:
    # we are doing a word search
    # we have to find one word: XMAS
    # the word search allows words to be horizontal, vertical, diagonal, written backwards, and overlapping
    # it is unusual, though, because we are not finding one xmas: but ALL of them
    # MMMSXXMASM
    # MSAMXMSMSA
    # AMXSXMAAMM
    # MSAMASMSMX
    # XMASAMXAMM
    # XXAMMXXAMA
    # SMSMSASXSS
    # SAXAMASAAA
    # MAMMMXMMMM
    # MXMXAXMASX

    # xmas appears 18 times in this grid

    # we are going to use a brute force approach
    # we are going to iterate through the grid
    # we are going to check all possible directions
    # we are going to check all possible lengths

    # we are going to use a 2D array to represent the grid
    # we are going to use a 2D array to represent the directions
    # we are going to use a 2D array to represent the word

    # convert the grid to a 2D array
    grid = file.read().splitlines()
    # convert the directions to a 2D array
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    # convert the word to a 2D array
    word = [[x for x in "XMAS"]]
    # initialize the count
    count = 0
    # iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # iterate through the directions
            for k in directions:
                # iterate through the word
                for l in range(len(word)):
                    # initialize the flag
                    flag = True
                    # iterate through the word
                    for m in range(len(word[l])):
                        # check if the word is out of bounds
                        if i + k[0] * m < 0 or i + k[0] * m >= len(grid) or j + k[1] * m < 0 or j + k[1] * m >= len(grid[i]):
                            flag = False
                            break
                        # check if the word is not the same
                        if grid[i + k[0] * m][j + k[1] * m] != word[l][m]:
                            flag = False
                            break
                    # check if the flag is true
                    if flag:
                        count += 1

    print(count)

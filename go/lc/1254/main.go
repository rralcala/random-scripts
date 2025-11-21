// You can edit this code!
// Click here and start typing.
package main

import (
	"fmt"
)

var grid = [][]int{{0, 0, 1, 1, 0, 1, 0, 0, 1, 0}, {1, 1, 0, 1, 1, 0, 1, 1, 1, 0}, {1, 0, 1, 1, 1, 0, 0, 1, 1, 0}, {0, 1, 1, 0, 0, 0, 0, 1, 0, 1}, {0, 0, 0, 0, 0, 0, 1, 1, 1, 0}, {0, 1, 0, 1, 0, 1, 0, 1, 1, 1}, {1, 0, 1, 0, 1, 1, 0, 0, 0, 1}, {1, 1, 1, 1, 1, 1, 0, 0, 0, 0}, {1, 1, 1, 0, 0, 1, 0, 1, 0, 1}, {1, 1, 1, 0, 1, 1, 0, 1, 1, 0}}

func main() {
	closedIsland(grid)
}

func closedIsland(grid [][]int) int {
	var islandNo = 2
	for i := 1; i < len(grid)-1; i++ {

		for j := 1; j < len(grid[i])-1; j++ {
			if grid[i][j] == 0 {
				if isIsland(grid, i, j, islandNo) {
					islandNo++
				}
			}
		}
	}
	fmt.Printf("%d", islandNo-2)
	return islandNo - 2
}

func isIsland(grid [][]int, i int, j int, mark int) bool {
	defer printMatrix(grid)
	grid[i][j] = mark
	var z, o = surroundings(grid, i, j, mark)
	if len(z)+o == 4 {
		if o < 4 {
			for k := 0; k < len(z); k++ {
				if !isIsland(grid, z[k][0], z[k][1], mark) {
					grid[i][j] = 0
					return false
				}
			}
		}
		return true
	}
	grid[i][j] = 0
	return false
}

func surroundings(grid [][]int, i int, j int, mark int) ([][]int, int) {
	var zeros [][]int
	var ones = 0
	if i == 0 || j == 0 || len(grid) == i+1 || len(grid[i]) == j+1 {
		return nil, 0
	}
	if grid[i-1][j] == 0 {
		zeros = append(zeros, []int{i - 1, j})
	} else if grid[i-1][j] == 1 || grid[i-1][j] == mark {
		ones++
	}
	if grid[i+1][j] == 0 {
		zeros = append(zeros, []int{i + 1, j})
	} else if grid[i+1][j] == 1 || grid[i+1][j] == mark {
		ones++
	}
	if grid[i][j-1] == 0 {
		zeros = append(zeros, []int{i, j - 1})
	} else if grid[i][j-1] == 1 || grid[i][j-1] == mark {
		ones++
	}
	if grid[i][j+1] == 0 {
		zeros = append(zeros, []int{i, j + 1})
	} else if grid[i][j+1] == 1 || grid[i][j+1] == mark {
		ones++
	}
	return zeros, ones
}

func printMatrix(mat [][]int) {
	for i := 0; i < len(mat); i++ {

		for j := 0; j < len(mat[i]); j++ {
			fmt.Printf("%d ", mat[i][j])

		}
		fmt.Println("")

	}
	fmt.Println("")
}

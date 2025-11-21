package main

import (
	"fmt"
	"strconv"
)

func main() {
	i := 321
	fmt.Printf("%d\n", reverse(i))
}

func reverse(x int) int {
	neg := 1
	slice := strconv.Itoa(x)
	if slice[0] == '-' {
		neg = -1
		slice = slice[1:]
	}

	output := ""
	for _, r := range slice {
		output = string(r) + output
	}
	out, err := strconv.Atoi(output)
	if err != nil || out > 2147483647 || out < -2147483648 {
		return 0
	}
	return out * neg
}

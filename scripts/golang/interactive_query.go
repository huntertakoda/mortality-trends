package query

import (
	"encoding/csv"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// runInteractiveQuery handles user-driven queries interactively
func RunInteractiveQuery() {
	// open the cleaned data file

	file, err := os.Open("cleaned_mortality_data.csv")
	if err != nil {
		fmt.Println("error opening file:", err)
		return
	}
	defer file.Close()

	// read csv content

	reader := csv.NewReader(file)
	data, err := reader.ReadAll()
	if err != nil {
		fmt.Println("error reading file:", err)
		return
	}

	// separate headers and rows

	headers := data[0]
	rows := data[1:]
	fmt.Println("interactive query tool - mortality dataset")
	fmt.Println("------------------------------------------")
	fmt.Println("columns available for queries:")
	for i, h := range headers {
		fmt.Printf("%d. %s\n", i+1, h)
	}

	// start query loop

	for {
		// prompt for user input

		fmt.Println("\nenter the column number to filter by (or 'exit' to quit):")
		var input string
		fmt.Scanln(&input)

		// check for exit condition

		if strings.ToLower(input) == "exit" {
			fmt.Println("exiting interactive query tool.")
			break
		}

		// parse column number

		colNum, err := strconv.Atoi(input)
		if err != nil || colNum < 1 || colNum > len(headers) {
			fmt.Println("invalid column number. please try again.")
			continue
		}
		colIndex := colNum - 1

		// prompt for filter condition

		fmt.Printf("enter a value to filter by for column '%s': ", headers[colIndex])
		var filterValue string
		fmt.Scanln(&filterValue)

		// execute query and display results

		results := filterRows(rows, colIndex, filterValue)
		if len(results) == 0 {
			fmt.Println("no matching records found.")
		} else {
			fmt.Printf("\nfound %d matching records:\n", len(results))
			for _, row := range results {
				fmt.Println(strings.Join(row, ", "))
			}
		}
	}
}

// filterRows filters rows based on a column index and value
func filterRows(rows [][]string, colIndex int, filterValue string) [][]string {
	var results [][]string

	// iterate over rows and apply filter

	for _, row := range rows {
		if len(row) > colIndex && strings.EqualFold(strings.TrimSpace(row[colIndex]), filterValue) {
			results = append(results, row)
		}
	}
	return results
}

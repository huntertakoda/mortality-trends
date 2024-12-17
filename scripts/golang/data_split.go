package split

import (
	"encoding/csv"
	"fmt"
	"os"
)

// RunDataSplit splits the dataset into two subsets: training and testing
func RunDataSplit() {
	// open the cleaned dataset
	file, err := os.Open("cleaned_mortality_data.csv")
	if err != nil {
		fmt.Println("error opening file:", err)
		return
	}
	defer file.Close()

	// read csv file
	reader := csv.NewReader(file)
	data, err := reader.ReadAll()
	if err != nil {
		fmt.Println("error reading file:", err)
		return
	}

	// split headers and rows
	headers := data[0]
	rows := data[1:]

	// determine split ratio (80/20 for training/testing)
	splitIndex := int(0.8 * float64(len(rows)))

	// create output files for training and testing
	writeSubset("train_data.csv", headers, rows[:splitIndex])
	writeSubset("test_data.csv", headers, rows[splitIndex:])

	fmt.Println("data successfully split into 'train_data.csv' and 'test_data.csv'")
}

// writes a subset of data to a new csv file
func writeSubset(filename string, headers []string, rows [][]string) {
	file, err := os.Create(filename)
	if err != nil {
		fmt.Println("error creating file:", filename, err)
		return
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	// write headers and rows
	writer.Write(headers)
	for _, row := range rows {
		writer.Write(row)
	}
}

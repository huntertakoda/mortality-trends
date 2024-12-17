package visuals

import (
	"encoding/csv"
	"fmt"
	"os"
	"strings"
)

// RunVisualizations creates simple ascii-based visualizations
func RunVisualizations() {
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

	// rows of data
	rows := data[1:]

	// count gender occurrences
	genderCounts := make(map[string]int)
	for _, row := range rows {
		gender := strings.TrimSpace(row[1])
		if gender != "" {
			genderCounts[gender]++
		}
	}

	// display visualizations
	fmt.Println("\ngender distribution visualization:")
	for gender, count := range genderCounts {
		bar := strings.Repeat("*", count/100) // scale bars for display
		fmt.Printf("%s: %s (%d)\n", gender, bar, count)
	}
}

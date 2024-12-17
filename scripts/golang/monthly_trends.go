package trends

import (
	"encoding/csv"
	"fmt"
	"os"
	"strings"
)

// RunMonthlyTrends calculates and displays monthly mortality trends
func RunMonthlyTrends() {
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

	// map to count deaths per month
	monthlyTrends := make(map[string]int)

	// iterate through rows and count by month
	for _, row := range rows {
		month := strings.TrimSpace(row[6])
		if month != "" {
			monthlyTrends[month]++
		}
	}

	// display results
	fmt.Println("\nmortality trends by month:")
	for month, count := range monthlyTrends {
		fmt.Printf("month %s: %d deaths\n", month, count)
	}
}

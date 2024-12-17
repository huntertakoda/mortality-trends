package topcauses

import (
	"encoding/csv"
	"fmt"
	"os"
	"sort"
	"strings"
)

// RunTopCauses identifies the most frequent causes of death
func RunTopCauses() {
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

	// map to count causes of death
	causeCounts := make(map[string]int)
	for _, row := range data[1:] {
		cause := strings.TrimSpace(row[4])
		causeCounts[cause]++
	}

	// sort causes by frequency
	type causeCount struct {
		Cause string
		Count int
	}
	var sortedCauses []causeCount
	for cause, count := range causeCounts {
		sortedCauses = append(sortedCauses, causeCount{cause, count})
	}
	sort.Slice(sortedCauses, func(i, j int) bool {
		return sortedCauses[i].Count > sortedCauses[j].Count
	})

	// display top causes
	fmt.Println("\ntop causes of death:")
	for i, entry := range sortedCauses {
		if i >= 5 {
			break
		}
		fmt.Printf("%s: %d occurrences\n", entry.Cause, entry.Count)
	}
}

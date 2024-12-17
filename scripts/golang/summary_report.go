package summary

import (
	"encoding/csv"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// RunSummaryReport generates the summary report for cleaned data
func RunSummaryReport() {
	// open the csv file
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

	// headers and rows
	headers := data[0]
	rows := data[1:] // skip headers

	fmt.Println("summary report for cleaned mortality data")
	fmt.Println("---------------------------------------")
	fmt.Println("columns:", headers)
	fmt.Printf("total rows: %d\n\n", len(rows))

	// variables for calculations
	var (
		totalAge, totalCoMorbidities, totalSocioIndex     float64
		infantCount, childCount, adultCount, elderlyCount int
		maleCount, femaleCount                            int
		validRows                                         int
	)

	// iterate over rows
	for _, row := range rows {
		if len(row) < 11 {
			fmt.Println("skipping invalid row:", row) // debug invalid rows
			continue
		}

		// parse age
		ageStr := strings.TrimSpace(row[0])
		age, err := strconv.ParseFloat(ageStr, 64)
		if err != nil {
			fmt.Println("invalid age value:", ageStr, "skipping row.")
			continue
		}

		// parse co-morbidity count
		coMorbiditiesStr := strings.TrimSpace(row[7])
		coMorbidities, err := strconv.ParseFloat(coMorbiditiesStr, 64)
		if err != nil {
			fmt.Println("invalid co-morbidity value:", coMorbiditiesStr, "skipping row.")
			continue
		}

		// parse socioeconomic index
		socioIndexStr := strings.TrimSpace(row[8])
		socioIndex, err := strconv.ParseFloat(socioIndexStr, 64)
		if err != nil {
			fmt.Println("invalid socioeconomic index:", socioIndexStr, "skipping row.")
			continue
		}

		// determine age group
		ageGroup := strings.TrimSpace(row[10])
		switch ageGroup {
		case "Infant":
			infantCount++
		case "Child":
			childCount++
		case "Adult":
			adultCount++
		case "Elderly":
			elderlyCount++
		default:
			fmt.Println("invalid age group:", ageGroup, "skipping row.")
			continue
		}

		// parse gender
		gender := strings.TrimSpace(row[1])
		if gender == "Male" {
			maleCount++
		} else if gender == "Female" {
			femaleCount++
		} else {
			fmt.Println("invalid gender:", gender, "skipping row.")
			continue
		}

		// accumulate totals
		totalAge += age
		totalCoMorbidities += coMorbidities
		totalSocioIndex += socioIndex
		validRows++
	}

	// compute averages
	if validRows > 0 {
		avgAge := totalAge / float64(validRows)
		avgCoMorbidities := totalCoMorbidities / float64(validRows)
		avgSocioIndex := totalSocioIndex / float64(validRows)

		// print summary report
		fmt.Printf("overall average age: %.2f\n", avgAge)
		fmt.Printf("overall average co-morbidity count: %.2f\n", avgCoMorbidities)
		fmt.Printf("overall average socioeconomic index: %.2f\n\n", avgSocioIndex)
	} else {
		fmt.Println("no valid rows processed.")
		return
	}

	// print age group counts
	fmt.Println("age group counts:")
	fmt.Printf("infants (0-1): %d\n", infantCount)
	fmt.Printf("children (2-18): %d\n", childCount)
	fmt.Printf("adults (19-64): %d\n", adultCount)
	fmt.Printf("elderly (65+): %d\n\n", elderlyCount)

	// print gender distribution
	fmt.Println("gender distribution:")
	fmt.Printf("male: %d\n", maleCount)
	fmt.Printf("female: %d\n", femaleCount)
}

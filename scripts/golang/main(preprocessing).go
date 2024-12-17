package main

import (
	"encoding/csv"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// open the csv file

	file, err := os.Open("synthetic_mortality_data.csv")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	// read csv

	reader := csv.NewReader(file)
	data, err := reader.ReadAll()
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// headers and data rows

	headers := data[0]
	headers = append(headers, "Age Group") // add new column
	rows := data[1:]                       // skip header row
	fmt.Println("Columns:", headers)
	fmt.Printf("Total rows: %d\n", len(rows))

	// variables for overall statistics

	var totalAge, validRows int
	var totalCoMorbidities, totalSocioeconomicIndex float64

	// variables for age group statistics

	ageGroupCounts := map[string]int{"Infant": 0, "Child": 0, "Adult": 0, "Elderly": 0}
	ageGroupSums := map[string]int{"Infant": 0, "Child": 0, "Adult": 0, "Elderly": 0}

	// gender counts for visualization

	genderCounts := map[string]int{"Male": 0, "Female": 0}

	// output rows for cleaned csv

	var cleanedRows [][]string
	cleanedRows = append(cleanedRows, headers) // add updated headers

	// loop through rows

	for _, row := range rows {
		if len(row) < 10 {
			fmt.Println("Skipping row with insufficient columns:", row)
			continue
		}

		// trim spaces and parse age

		ageStr := strings.TrimSpace(row[0])
		age, err := strconv.ParseFloat(ageStr, 64)
		if err != nil || age < 0 {
			fmt.Println("Invalid age value:", ageStr, "skipping row.")
			continue
		}

		// parse gender

		gender := strings.TrimSpace(row[1])
		if gender != "Male" && gender != "Female" {
			fmt.Println("Invalid gender value:", gender, "skipping row.")
			continue
		}
		genderCounts[gender]++

		// parse co-morbidity count

		coMorbiditiesStr := strings.TrimSpace(row[7])
		coMorbidities, err := strconv.ParseFloat(coMorbiditiesStr, 64)
		if err != nil {
			fmt.Println("Invalid co-morbidity value:", coMorbiditiesStr, "skipping row.")
			continue
		}

		// parse socioeconomic index

		socioeconomicStr := strings.TrimSpace(row[8])
		socioeconomicIndex, err := strconv.ParseFloat(socioeconomicStr, 64)
		if err != nil {
			fmt.Println("Invalid socioeconomic index value:", socioeconomicStr, "skipping row.")
			continue
		}

		// determine age group

		var ageGroup string
		if age <= 1 {
			ageGroup = "Infant"
		} else if age <= 18 {
			ageGroup = "Child"
		} else if age <= 64 {
			ageGroup = "Adult"
		} else {
			ageGroup = "Elderly"
		}
		ageGroupCounts[ageGroup]++
		ageGroupSums[ageGroup] += int(age)

		// append new age group to the row

		row = append(row, ageGroup)
		cleanedRows = append(cleanedRows, row)

		// overall stats

		totalAge += int(age)
		totalCoMorbidities += coMorbidities
		totalSocioeconomicIndex += socioeconomicIndex
		validRows++
	}

	// compute + print overall averages

	if validRows > 0 {
		avgAge := float64(totalAge) / float64(validRows)
		avgCoMorbidities := totalCoMorbidities / float64(validRows)
		avgSocioeconomicIndex := totalSocioeconomicIndex / float64(validRows)
		fmt.Printf("\nOverall average age: %.2f\n", avgAge)
		fmt.Printf("Overall average co-morbidity count: %.2f\n", avgCoMorbidities)
		fmt.Printf("Overall average socioeconomic index: %.2f\n", avgSocioeconomicIndex)
	}

	// print age group statistics

	fmt.Println("\nAge group counts and averages:")
	for group, count := range ageGroupCounts {
		if count > 0 {
			avgAge := float64(ageGroupSums[group]) / float64(count)
			fmt.Printf("%s: Count = %d, Average Age = %.2f\n", group, count, avgAge)
		} else {
			fmt.Printf("%s: No valid data.\n", group)
		}
	}

	// print gender distribution

	fmt.Println("\nGender distribution:")
	for gender, count := range genderCounts {
		fmt.Printf("%s: Count = %d\n", gender, count)
	}

	// saving

	outputFile, err := os.Create("cleaned_mortality_data.csv")
	if err != nil {
		fmt.Println("Error creating file:", err)
		return
	}
	defer outputFile.Close()

	writer := csv.NewWriter(outputFile)
	defer writer.Flush()

	for _, row := range cleanedRows {
		if err := writer.Write(row); err != nil {
			fmt.Println("Error writing row:", err)
			return
		}
	}

	fmt.Println("\nCleaned data saved to 'cleaned_mortality_data.csv'")
}

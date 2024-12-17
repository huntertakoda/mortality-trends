package correlations

import (
	"encoding/csv"
	"fmt"
	"math"
	"os"
	"reflect"
	"sort"
	"strconv"
	"strings"
)

// computePearson calculates the Pearson correlation coefficient between two slices

func computePearson(x, y []float64) float64 {
	if len(x) != len(y) || len(x) == 0 {
		return 0
	}

	// variables for summing values
	var sumX, sumY, sumXY, sumX2, sumY2 float64
	n := float64(len(x))

	// calculate components for the correlation formula
	for i := 0; i < len(x); i++ {
		sumX += x[i]
		sumY += y[i]
		sumXY += x[i] * y[i]
		sumX2 += x[i] * x[i]
		sumY2 += y[i] * y[i]
	}

	// calculate numerator and denominator
	numerator := sumXY - (sumX * sumY / n)
	denominator := math.Sqrt((sumX2 - sumX*sumX/n) * (sumY2 - sumY*sumY/n))

	// handle division by zero
	if denominator == 0 {
		return 0
	}

	return numerator / denominator
}

// RunCorrelations analyzes correlations in the dataset and prints a summary

func RunCorrelations() {
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

	// parse headers and rows

	headers := data[0]
	rows := data[1:]
	fmt.Println("columns:", headers)

	// target numeric fields for correlation analysis
	// age, co-morbidity count, and socioeconomic index

	var fields = map[string]int{
		"Age":                 0,
		"Co-morbidity Count":  8,
		"Socioeconomic Index": 9,
	}

	// dynamically store numeric values for analysis
	fieldValues := make(map[string][]float64)
	for key := range fields {
		fieldValues[key] = []float64{}
	}

	// parse rows and collect numeric values
	for _, row := range rows {
		for field, index := range fields {
			val, err := strconv.ParseFloat(strings.TrimSpace(row[index]), 64)
			if err == nil {
				fieldValues[field] = append(fieldValues[field], val)
			}
		}
	}

	// compute pairwise correlations
	fmt.Println("\ncorrelation analysis:")

	type correlationResult struct {
		Pair  string
		Value float64
	}

	results := []correlationResult{}
	keys := reflect.ValueOf(fields).MapKeys()

	// iterate over all pairs of numeric fields
	for i := 0; i < len(keys); i++ {
		for j := i + 1; j < len(keys); j++ {
			xKey := keys[i].String()
			yKey := keys[j].String()
			correlation := computePearson(fieldValues[xKey], fieldValues[yKey])

			// store correlation results
			results = append(results, correlationResult{
				Pair:  fmt.Sprintf("%s - %s", xKey, yKey),
				Value: correlation,
			})
		}
	}

	// sort results by absolute correlation value
	sort.Slice(results, func(i, j int) bool {
		return math.Abs(results[i].Value) > math.Abs(results[j].Value)
	})

	// print sorted correlation results
	for _, result := range results {
		fmt.Printf("%s: %.4f\n", result.Pair, result.Value)
	}
}

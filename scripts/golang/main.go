package main

import (
	"mortalityproject2/correlations"
	"mortalityproject2/query"
	"mortalityproject2/split"
	"mortalityproject2/summary"
	"mortalityproject2/topcauses"
	"mortalityproject2/trends"
	"mortalityproject2/visuals"
)

func main() {
	// run summary report
	summary.RunSummaryReport()

	// run data split analysis
	split.RunDataSplit()

	// run interactive queries
	query.RunInteractiveQuery()

	// run monthly trends analysis
	trends.RunMonthlyTrends()

	// run top causes of death analysis
	topcauses.RunTopCauses()

	// run correlations analysis
	correlations.RunCorrelations()

	// run visualizations
	visuals.RunVisualizations()
}

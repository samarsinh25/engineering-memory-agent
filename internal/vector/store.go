package cli

import (
	"fmt"
	"github.com/spf13/cobra"
)

var SearchCmd = &cobra.Command{
	Use:   "search [query]",
	Short: "Search logs semantically",
	Args:  cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		query := args[0]
		fmt.Println("Searching logs for:", query)
		// Load vectors, calculate cosine similarity, return top 3
	},
}

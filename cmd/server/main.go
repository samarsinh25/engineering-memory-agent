package main

import (
	"engineering-memory-agent/internal/cli"
	"github.com/joho/godotenv"
	"github.com/spf13/cobra"
	"log"
)

func init() {
	if err := godotenv.Load(); err != nil {
		log.Fatal("No .env file found")
	}
}

func main() {
	rootCmd := &cobra.Command{Use: "ema"}
	rootCmd.AddCommand(cli.SearchCmd)
	rootCmd.Execute()
}

#!/usr/bin/env bash
# Script to run doctests on all Python scripts in the scripts/ directory
# Define colors for display
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m'

echo "============================================================"
echo -e "${GREEN}Running doctests for all Python modules${NC}"
echo "============================================================"

# Make the Python script executable
chmod +x tests/run_doctests.py

# Run the Python script and capture its output
OUTPUT=$(python3 tests/run_doctests.py)
EXIT_CODE=$?

# Display the output
echo "$OUTPUT"

echo "============================================================"

if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✅ All tests passed successfully!${NC}"
else
    echo -e "${RED}❌ Some tests failed.${NC}"
    
    # Extract and display the failed functions section
    if echo "$OUTPUT" | grep -q "Failed functions by file:"; then
        echo -e "\n${YELLOW}Summary of failures:${NC}"
        echo "$OUTPUT" | sed -n '/Failed functions by file:/,/^$/p' | grep -v "Failed functions by file:"
    fi
fi
echo "============================================================"

# Return the exit code from the Python script
exit $EXIT_CODE 
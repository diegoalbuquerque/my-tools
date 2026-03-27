#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
RESET='\033[0m'

printf "${BOLD}${CYAN}SSLS - Simple Script LiteLLM SCAN${RESET}\n\n"

printf "${BOLD}[+] Verifying if LiteLLM is installed...${RESET}\n"
LITELLM_INFO=$(pip show litellm 2>/dev/null)

if [ -z "$LITELLM_INFO" ]; then
    printf "${GREEN}[OK] LiteLLM not installed${RESET}\n\n"
else
    VERSION=$(echo "$LITELLM_INFO" | grep "Version:" | awk '{print $2}')
    printf "${YELLOW}[!] LiteLLM found! Version: %s${RESET}\n" "$VERSION"

    if [[ "$VERSION" == "1.82.7" || "$VERSION" == "1.82.8" ]]; then
        printf "${RED}${BOLD}[!] CRITICAL: COMPROMISED VERSION${RESET}\n\n"
    else
        printf "${GREEN}[OK] Safe version${RESET}\n\n"
    fi
fi

printf "${BOLD}[+] Scanning installed packages for litellm dependency...${RESET}\n"

pip list --format=columns | awk 'NR>2 {print $1}' | while read -r pkg; do
    printf "${YELLOW} ... analysing $pkg \n"
    DEPS=$(pip show "$pkg" 2>/dev/null | grep "Requires:" | grep -i "litellm")
    if [ -n "$DEPS" ]; then
        printf "${RED}[!] '%s' depends on litellm${RESET}\n" "$pkg"
    fi
done

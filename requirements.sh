#!/bin/bash

printf "\e[32;5mChecking requirements...\e[0m\n"
echo ""
apt-get upgrade && apt-get update
apt-get install php && apt-get install python* && apt-get install openssh
echo ""
printf "\e[32;5mDone! Happy Phishing!!\e[0m\n"
echo ""

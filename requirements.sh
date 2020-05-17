#!/bin/bash

printf "\e[34;5mChecking requirements..."
echo ""
apt-get upgrade && apt-get update
apt-get install openssh && apt-get install php && apt-get install python*
echo ""
printf "\e[34;5mDone! Happy Phishing!!\e[0m\n"
echo ""
# Makefile for Go Microservice

.PHONY: build test run docker-build

build:
	go build -o bin/api ./cmd/api

test:
	go test -v ./...

run:
	go run ./cmd/api

docker-build:
	docker build -t go-microservice -f deploy/docker/Dockerfile .

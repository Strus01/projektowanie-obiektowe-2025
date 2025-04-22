package models

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

type Weather struct {
	Temperature float64 `json:"temperature"`
}

type APIResponse struct {
	Current Weather `json:"current_weather"`
}

func FetchWeatherFromAPI() (*APIResponse, error) {
	lat := "50.049683"
	lon := "19.944544"
	url := fmt.Sprintf("https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&current_weather=true", lat, lon)

	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)

	var data APIResponse
	if err := json.Unmarshal(body, &data); err != nil {
		return nil, err
	}

	return &data, nil
}

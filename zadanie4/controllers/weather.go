package controllers

import (
	"net/http"
	"zadanie4/models"

	"github.com/labstack/echo/v4"
)

func GetWeather(c echo.Context) error {
	data, err := models.FetchWeatherFromAPI()
	if err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{"error": "Could not download weather data."})
	}
	return c.JSON(http.StatusOK, data)
}

package logging

import (
	"bytes"
	"encoding/json"
	"strings"
	"testing"
)

func TestLoggerLevels(t *testing.T) {
	tests := []struct {
		name     string
		level    Level
		logFunc  func(*Logger, string)
		expected bool
	}{
		{"debug at debug level", LevelDebug, func(l *Logger, msg string) { l.Debug(msg) }, true},
		{"info at debug level", LevelDebug, func(l *Logger, msg string) { l.Info(msg) }, true},
		{"debug at info level", LevelInfo, func(l *Logger, msg string) { l.Debug(msg) }, false},
		{"info at info level", LevelInfo, func(l *Logger, msg string) { l.Info(msg) }, true},
		{"warn at error level", LevelError, func(l *Logger, msg string) { l.Warn(msg) }, false},
		{"error at error level", LevelError, func(l *Logger, msg string) { l.Error(msg) }, true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			buf := &bytes.Buffer{}
			logger := New(WithOutput(buf), WithLevel(tt.level))
			tt.logFunc(logger, "test message")
			hasOutput := buf.Len() > 0
			if hasOutput != tt.expected {
				t.Errorf("expected output=%v, got output=%v", tt.expected, hasOutput)
			}
		})
	}
}

func TestLoggerJSONMode(t *testing.T) {
	buf := &bytes.Buffer{}
	logger := New(WithOutput(buf), WithLevel(LevelDebug), WithJSONMode(true))
	logger.Info("test message", map[string]interface{}{"key": "value"})

	var entry Entry
	if err := json.Unmarshal(buf.Bytes(), &entry); err != nil {
		t.Fatalf("failed to parse JSON output: %v", err)
	}

	if entry.Level != "INFO" {
		t.Errorf("expected level=INFO, got level=%s", entry.Level)
	}
	if entry.Message != "test message" {
		t.Errorf("expected message='test message', got message='%s'", entry.Message)
	}
	if entry.Fields["key"] != "value" {
		t.Errorf("expected fields.key='value', got fields.key='%v'", entry.Fields["key"])
	}
}

func TestLoggerWithFields(t *testing.T) {
	buf := &bytes.Buffer{}
	logger := New(WithOutput(buf), WithLevel(LevelDebug), WithFields(map[string]interface{}{"service": "test"}))
	childLogger := logger.With(map[string]interface{}{"component": "child"})
	childLogger.Info("test")

	output := buf.String()
	if !strings.Contains(output, "service") {
		t.Error("expected output to contain 'service' field")
	}
	if !strings.Contains(output, "component") {
		t.Error("expected output to contain 'component' field")
	}
}

func TestLevelString(t *testing.T) {
	tests := []struct {
		level    Level
		expected string
	}{
		{LevelDebug, "DEBUG"},
		{LevelInfo, "INFO"},
		{LevelWarn, "WARN"},
		{LevelError, "ERROR"},
		{Level(99), "UNKNOWN"},
	}

	for _, tt := range tests {
		t.Run(tt.expected, func(t *testing.T) {
			if got := tt.level.String(); got != tt.expected {
				t.Errorf("expected %s, got %s", tt.expected, got)
			}
		})
	}
}

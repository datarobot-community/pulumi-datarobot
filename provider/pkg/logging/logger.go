// Package logging provides structured logging utilities for the DataRobot Pulumi provider.
package logging

import (
	"encoding/json"
	"fmt"
	"io"
	"os"
	"sync"
	"time"
)

// Level represents the severity level of a log message.
type Level int

const (
	LevelDebug Level = iota
	LevelInfo
	LevelWarn
	LevelError
)

func (l Level) String() string {
	switch l {
	case LevelDebug:
		return "DEBUG"
	case LevelInfo:
		return "INFO"
	case LevelWarn:
		return "WARN"
	case LevelError:
		return "ERROR"
	default:
		return "UNKNOWN"
	}
}

// Entry represents a structured log entry.
type Entry struct {
	Timestamp string                 `json:"timestamp"`
	Level     string                 `json:"level"`
	Message   string                 `json:"message"`
	Fields    map[string]interface{} `json:"fields,omitempty"`
}

// Logger provides structured logging capabilities.
type Logger struct {
	mu       sync.Mutex
	output   io.Writer
	level    Level
	fields   map[string]interface{}
	jsonMode bool
}

// Option configures a Logger.
type Option func(*Logger)

// WithOutput sets the output writer.
func WithOutput(w io.Writer) Option {
	return func(l *Logger) {
		l.output = w
	}
}

// WithLevel sets the minimum log level.
func WithLevel(level Level) Option {
	return func(l *Logger) {
		l.level = level
	}
}

// WithJSONMode enables JSON output format.
func WithJSONMode(enabled bool) Option {
	return func(l *Logger) {
		l.jsonMode = enabled
	}
}

// WithFields adds default fields to all log entries.
func WithFields(fields map[string]interface{}) Option {
	return func(l *Logger) {
		for k, v := range fields {
			l.fields[k] = v
		}
	}
}

// New creates a new Logger with the given options.
func New(opts ...Option) *Logger {
	l := &Logger{
		output:   os.Stderr,
		level:    LevelInfo,
		fields:   make(map[string]interface{}),
		jsonMode: false,
	}
	for _, opt := range opts {
		opt(l)
	}
	return l
}

// Default returns a default logger instance.
func Default() *Logger {
	return New(
		WithLevel(getLogLevelFromEnv()),
		WithJSONMode(os.Getenv("PULUMI_LOG_JSON") == "true"),
	)
}

func getLogLevelFromEnv() Level {
	switch os.Getenv("PULUMI_LOG_LEVEL") {
	case "debug", "DEBUG":
		return LevelDebug
	case "warn", "WARN":
		return LevelWarn
	case "error", "ERROR":
		return LevelError
	default:
		return LevelInfo
	}
}

// With returns a new Logger with additional fields.
func (l *Logger) With(fields map[string]interface{}) *Logger {
	newLogger := &Logger{
		output:   l.output,
		level:    l.level,
		fields:   make(map[string]interface{}),
		jsonMode: l.jsonMode,
	}
	for k, v := range l.fields {
		newLogger.fields[k] = v
	}
	for k, v := range fields {
		newLogger.fields[k] = v
	}
	return newLogger
}

func (l *Logger) log(level Level, msg string, fields map[string]interface{}) {
	if level < l.level {
		return
	}

	l.mu.Lock()
	defer l.mu.Unlock()

	allFields := make(map[string]interface{})
	for k, v := range l.fields {
		allFields[k] = v
	}
	for k, v := range fields {
		allFields[k] = v
	}

	entry := Entry{
		Timestamp: time.Now().UTC().Format(time.RFC3339),
		Level:     level.String(),
		Message:   msg,
		Fields:    allFields,
	}

	if l.jsonMode {
		data, _ := json.Marshal(entry)
		fmt.Fprintln(l.output, string(data))
	} else {
		if len(allFields) > 0 {
			fmt.Fprintf(l.output, "[%s] %s: %s %v\n", entry.Timestamp, entry.Level, entry.Message, allFields)
		} else {
			fmt.Fprintf(l.output, "[%s] %s: %s\n", entry.Timestamp, entry.Level, entry.Message)
		}
	}
}

// Debug logs a debug message.
func (l *Logger) Debug(msg string, fields ...map[string]interface{}) {
	var f map[string]interface{}
	if len(fields) > 0 {
		f = fields[0]
	}
	l.log(LevelDebug, msg, f)
}

// Info logs an info message.
func (l *Logger) Info(msg string, fields ...map[string]interface{}) {
	var f map[string]interface{}
	if len(fields) > 0 {
		f = fields[0]
	}
	l.log(LevelInfo, msg, f)
}

// Warn logs a warning message.
func (l *Logger) Warn(msg string, fields ...map[string]interface{}) {
	var f map[string]interface{}
	if len(fields) > 0 {
		f = fields[0]
	}
	l.log(LevelWarn, msg, f)
}

// Error logs an error message.
func (l *Logger) Error(msg string, fields ...map[string]interface{}) {
	var f map[string]interface{}
	if len(fields) > 0 {
		f = fields[0]
	}
	l.log(LevelError, msg, f)
}

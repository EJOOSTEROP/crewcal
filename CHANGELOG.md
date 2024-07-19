# Changelog
All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [Unreleased]

- Consider downgrading Python requirement (at least to 3.10, but I dont know how low it can gowhere)

## [0.8.5]

### Added
- Hotel information

### Changed
- Upgrade LLM to GPT 4o mini

## [0.8.4]

### Added
- Show actual cost - as calculated by langchain - after call. Note: does not seem to work for gpt-4o.

### Changed
- Catch error and show warning in log when command is run without OPENAI_API_KEY being set.

## [0.8.3]

### Fixed
- +1 for next date now no longer causing json issues. Stopped working with the same OpenAI model after previous fix.

## [0.8.2]

### Fixed
- Arrivals on next day are correctly reflected again. Stopped working with the same OpenAI model.

### Changed
- Adding extract completed message using Halo (spinner)

## [0.8.1]

### Fixed
- Error with reading and saving files.

## [0.8.0]

### Added
- Main functionality to extract schedule information using gpt 3.5 turbo.
- Serialize to .ics format.
- CLI

### Fixed
- None

### Changed
- None

### Removed
- None

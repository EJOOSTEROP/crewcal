# Changelog
All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [Unreleased]

- Consider downgrading Python requirement (at least to 3.10, but I dont know how low it can gowhere)

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

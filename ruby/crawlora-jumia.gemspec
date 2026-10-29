require_relative "lib/crawlora/jumia/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-jumia"
  spec.version = Crawlora::Jumia::VERSION
  spec.summary = "Jumia API client for Crawlora (8 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Jumia API. Covers country and category discovery, product search, and product details across 8 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=jumia-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-jumia", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-jumia/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end

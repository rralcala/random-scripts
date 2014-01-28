#!/bin/ruby
require 'openssl'
require 'net/http'

#From rubydoc example but with ssl support and print as arrives
def fetch(uri_str, limit = 10)
  # You should choose a better exception.
  raise Net::HTTPError, 'too many HTTP redirects' if limit == 0

  uri = URI(uri_str)
  http = Net::HTTP.new(uri.host, uri.port)
  if uri.is_a? URI::HTTPS
    http.use_ssl = true
    http.verify_mode = OpenSSL::SSL::VERIFY_NONE
  end

  http.get2(uri.request_uri) do |response|

    case response
      when Net::HTTPSuccess then
        response.read_body do |segment|
          print segment
        end
      when Net::HTTPRedirection then
        location = response['location']
        warn "redirected to #{location}"
        fetch(location, limit - 1)
      else
        warn response.value
      end
    end
end

fetch(ARGV[0])

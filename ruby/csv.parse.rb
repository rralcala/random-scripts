require 'csv'
require 'get_impaired_kernel'
require 'date'

csv_text = File.read('./select-diagnostics(2).csv')
csv = CSV.parse(csv_text)
csv.each do |line|
    Date.parse line[1]

end

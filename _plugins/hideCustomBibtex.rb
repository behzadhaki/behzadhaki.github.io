# encoding: utf-8
 module Jekyll
  module HideCustomBibtex
    def hideCustomBibtex(input)
	  keywords = @context.registers[:site].config['filtered_bibtex_keywords']

	  keywords.each do |keyword|
		input = input.gsub(/^.*#{keyword}.*$\n/, '')
	  end

      # Strip equal-contrib markers (* ^ and unicode dagger/pilcrow) from author names
      input = input.gsub(/(\p{L})[*\^†¶]/, '\1')

      return input
    end
  end
end

Liquid::Template.register_filter(Jekyll::HideCustomBibtex)

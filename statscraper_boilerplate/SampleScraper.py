# encoding: utf-8
from statscraper import BaseScraper


class SampleScraper(BaseScraper):
    """Sample scraper for statscraper boilerplate."""

    def _fetch_allowed_values(self, dimension):
        """Yield the allowed values for <dimension>."""
        pass

    def _fetch_dimensions(self, dataset):
        """Yield the available dimensions in <dataset>."""
        pass

    def _fetch_data(self, dataset, query=None):
        """Yield rows from <dataset>."""
        pass

    def _fetch_itemslist(self, item):
        """Yield a collection or dataset at
        the current cursor position."""
        pass

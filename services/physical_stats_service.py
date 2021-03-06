import hashlib
import os


class PhysicalStatsService:

    def __init__(self, physical_stats_repo, user_repo):
        self.physical_stats_repo = physical_stats_repo
        self.user_repo = user_repo

    def get_user_info(self, physical_stats):
        return self.user_repo.get_user_by_id(physical_stats.user_id)

    def get_physical_stats_by_user_id(self, user_id):
        stats = next(
            filter(lambda stat: stat.user_id == user_id, self.physical_stats_repo.get_all_physical_stats()), None)

        return stats

    def delete_physical_stats(self, id):
        physical_stats = self.physical_stats_repo.get_physical_stats_by_id(id)
        self.physical_stats_repo.delete_physical_stats(physical_stats)
        return physical_stats
    def create_new_physical_stats(self, physical_stats):
        if physical_stats.user_id in [s.user_id for s in self.physical_stats_repo.get_all_physical_stats()]:
            raise Exception("For that user physical stats already exists.")
        self.physical_stats_repo.create_physical_stats(physical_stats)
    def update_physical_stats(self):
        self.physical_stats_repo.safe_update_changes()
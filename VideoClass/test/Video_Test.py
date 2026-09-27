import unittest
from video import Video

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.video = Video()

    def test_that_when_i_play_video_starts_playing(self):
        self.assertEqual("Now Playing: Avatar",self.video.play())

    def test_that_when_i_advance_playback_move_forward_by_number_of_minutes(self):
        self.video.advance(5)
        self.assertEqual(5, self.video.playback)

    def test_that_when_i_advance_i_cant_advance_negative_minutes(self):
        self.video.advance(-5)
        self.assertEqual(0, self.video.playback)

    def test_that_when_i_advance_i_advance_i_cant_advance_more_than_duration_of_video(self):
        for _ in range(95): self.video.advance(1)
        self.assertEqual(90, self.video.playback)

    def test_that_when_playback_equals_duration_of_video_video_is_finished(self):
        for _ in range(95): self.video.advance(1)
        self.assertTrue(self.video.is_finished())

    def test_that_when_i_restart_playback_returns_to_beginning(self):
        self.video.advance(50)
        self.assertEqual(self.video.playback, 50)
        self.video.restart()
        self.assertEqual(0, self.video.playback)

    def test_that_when_i_check_time_remaining_returns_minutes_left_to_end_of_video(self):
        self.video.advance(50)
        self.assertEqual(40, self.video.time_remaining())

if __name__ == '__main__':
    unittest.main()

class Solution(object):
    def largestAltitude(self, gain):
        do_cao_hien_tai = 0
        do_cao_lon_nhat = 0

        for thay_doi in gain:
            do_cao_hien_tai = do_cao_hien_tai + thay_doi

            if do_cao_hien_tai > do_cao_lon_nhat:
                do_cao_lon_nhat = do_cao_hien_tai

        return do_cao_lon_nhat


# # Step 5: Copy files to Hadoop
# echo "Copying files to Hadoop..."
# docker exec -it resourcemanager /bin/bash -c "\
#     hadoop fs -mkdir /energy-data && \
#     cd /opt/energy-data && \
#     hadoop fs -put owid-energy-data.csv /energy-data/ && \
#     hadoop fs -ls /energy-data/"
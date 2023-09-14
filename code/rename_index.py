

with open('./migrations/versions/5fb480ac2376_.py') as f:
    count = 0
    lines = []
    down_grade = False
    while True:
        count += 1
        line = f.readline()
        if not line:
            break
        if line.startswith('def downgrade():'):
            down_grade = True

        if not down_grade:
            table_feature = '    with op.batch_alter_table(\''
            if line.startswith(table_feature):
                table_name = line[len(table_feature): line.find('\'', len(table_feature))]
                print(f'table_name: {table_name}')

            index_feature = '        batch_op.create_index(\''
            if line.startswith(index_feature):
                new_index_pos_end = line.find('\'', len(index_feature))
                new_index_name = line[len(index_feature): new_index_pos_end]
                print(f'new_index_name: {new_index_name}')
                old_index_pos_start = line.find('[\'', new_index_pos_end + 1)
                old_index_name = line[old_index_pos_start + 2: line.find('\']', old_index_pos_start + 3)]
                print(f'old_index_name: {old_index_name}')
                new_line = \
                    f'        op.execute(\'alter table {table_name} rename index {old_index_name} to {new_index_name}\')\n'
                print(f'{count}\n')
                lines.append(new_line)
                continue

        lines.append(line)

    with open('./rename_index_output.py', 'w') as f:
        f.writelines(lines)

    print("Line count=: {}".format(count))
